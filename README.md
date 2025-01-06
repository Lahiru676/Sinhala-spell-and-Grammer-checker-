# Sinhala-spell-and-Grammer-checker-
# Spell and Grammar Checker

## Overview
The Spell and Grammar Checker is a tool designed to analyze and correct text by identifying and addressing grammatical and spelling errors. It supports batch processing and is capable of handling multilingual text. This project is particularly useful for writers, students, and anyone who wants to improve the quality of their written content.

## Features
- **Grammar Correction**: Detects and corrects grammatical errors in text.
- **Spelling Correction**: Identifies and fixes misspelled words.
- **Batch Processing**: Processes multiple texts simultaneously.
- **Custom Training Data**: Supports loading of custom training data for specialized use cases.
- **Multilingual Support**: Can work with various languages.

## Technologies Used
- **Python**: Core programming language.
- **OpenAI API**: Powers the text analysis and corrections.
- **Google Colab**: For seamless execution and integration.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/spell-and-grammar-checker.git
   ```
2. Navigate to the project directory:
   ```bash
   cd spell-and-grammar-checker
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Setup
1. **Set Your OpenAI API Key**:
   - Save your OpenAI API key as a secret in your Google Colab notebook or as an environment variable.
   - Example:
     ```python
     from google.colab import userdata
     api_key = userdata.get('OPENAI_API_KEY')
     ```

2. **Load Training Data**:
   - Ensure your training data file (e.g., `training_data.json`) is stored in an accessible location (e.g., Google Drive).
   - Example:
     ```python
     checker.load_training_data("/content/drive/MyDrive/sinhala_grammar_training.json")
     ```



### Outputs
- **Input**: The original text provided.
- **Analysis**: Detailed corrections and suggestions for improvement.

## File Structure
```
spell-and-grammar-checker/
├── AI_approch    # Core logic for spell and grammar checking
├── Datasets.json    # Example training data file
├── requirements.txt      # Project dependencies
├── README.md             # Project documentation
└── examples/             # Example scripts and usage scenarios
```

## Contributing
https://github.com/Lahiru676  -2020E024
https://github.com/Chamara23  -2019E022


Contributions are welcome! If you'd like to improve the project, feel free to:
1. Fork the repository.
2. Create a feature branch.
3. Submit a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For questions or feedback, feel free to reach out:
- **Email**: lubulathwaththa676@gmail.com
- **GitHub**: [yourusername](https://github.com/Lahiru676)

---
Thank you for using the Spell and Grammar Checker! 🚀

