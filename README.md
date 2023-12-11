# GitHub Issue Processor

## Overview
The GitHub Issue Processor is an automated action that enhances the quality and clarity of newly opened issues on a GitHub repository. Utilizing OpenAI's GPT-4 model, this action automatically processes each new issue to:

1. Summarize and improve the content of the issue.
2. Suggest relevant labels for the issue.
3. Generate questions to clarify and refine the issue's focus.

## Features
- **Customizable AI Model**: Choose which OpenAI model to use.
- **Flexible Token Limit**: Set the maximum number of tokens for the AI's response.
- **Custom Prompts**: Define your own prompt structure for AI processing.

## Getting Started
To use this GitHub Action in your repository, follow these steps:

### 1. Setup the Action
- Place the `.github/workflows/issue-processor.yml` file in your repository.
- Ensure the script `.github/scripts/process_issue.py` is also added to your repository.

### 2. Configure GitHub Secrets
- Add `GITHUB_TOKEN` with your GitHub token.
- Add `OPENAI_API_KEY` with your OpenAI API key.

### 3. Customize the Action (Optional)
In the `issue-processor.yml` file, you can specify:
- `ai_model`: The OpenAI model to use (default: 'text-davinci-004').
- `max_tokens`: The maximum number of tokens for the AI response (default: 150).
- `ai_prompt`: The custom prompt template for AI processing.

Example configuration:

```yaml
name: Test Issue Processor
on:
  issues:
    types: [opened]
jobs:
  test-job:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v2
      - name: Test Issue Processor
        uses: lduf/issueGPT@main
        with:
          ai_model: 'gpt-4-1106-preview'
          max_tokens: '1000'

```

## Usage
Once set up, the action will automatically run whenever a new issue is opened in your repository. It processes the issue content using the specified OpenAI model and updates the issue with a summary, suggested labels, and follow-up questions.

## Contributing
Contributions to this project are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) for more information on how to contribute.

## License
This project is licensed under the [MIT License](LICENSE.md).

## Support
If you encounter any problems or have suggestions, please open an issue or contact the repository maintainers.
