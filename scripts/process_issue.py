import os
import openai
from github import Github

def main():
    # Initialization
    g = Github(os.getenv('GITHUB_TOKEN'))
    openai.api_key = os.getenv('OPENAI_API_KEY')
    
    # Custom parameters
    ai_model = os.getenv('AI_MODEL', 'gpt-4-1106-preview')
    max_tokens = int(os.getenv('MAX_TOKENS', 1000))

    # Get issue information
    repo = g.get_repo(os.getenv('GITHUB_REPOSITORY'))
    issue = repo.get_issue(number=int(os.getenv('GITHUB_ISSUE_NUMBER')))

    user_login = issue.user.login
    original_issue_text = issue.body

    # Construct the AI prompt
    ai_prompt = (
        f"Please rephrase the following issue to make it clearer and provide additional context where necessary:\n{original_issue_text}\n\n"
        "Identify the type of this issue. Is it a documentation update, a bug report, a feature request, or something else?\n\n"
        f"Tag the user @{user_login} who created this issue and list a few questions that could help clarify the issue for better understanding and resolution."
    )

    # OpenAI ChatCompletion request
    response = openai.ChatCompletion.create(
        model=ai_model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant experienced in software development and issue tracking. Your task is to analyze GitHub issues, provide clear and concise summaries, categorize them accurately (e.g., bug, feature request, documentation), and generate relevant questions to clarify each issue for better understanding."},
            {"role": "user", "content": ai_prompt}
        ],
        max_tokens=max_tokens
    )

    # Update the issue with the response
    issue.create_comment(f"AI-Assisted Response:\n{response.choices[0].message['content']}")

if __name__ == "__main__":
    main()