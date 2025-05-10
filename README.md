# 🚀 Naukri.com Job Scraper

![GitHub stars](https://img.shields.io/github/stars/pawankumar941394/naukri-scraper?style=social)
![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A powerful Python tool for scraping job listings from Naukri.com, allowing you to search for jobs by title and collect detailed information in a CSV format.

## 📋 Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Sample Output](#sample-output)
- [Contributing](#contributing)
- [Connect With Me](#connect-with-me)
- [License](#license)

## ✨ Features

- 🔍 Search for jobs by title on Naukri.com
- 📄 Export job listings to CSV files for easy analysis
- 📊 Extract comprehensive job details including:
  - Job title
  - Company name
  - Job description
  - Company logo URL
  - Experience requirements
  - Job location
  - Posted date
  - Salary information
  - Skills required
  - Job ID and URL
- 📱 User-friendly command-line interface
- 📃 Page navigation functionality

## 📦 Requirements

- Python 3.6+
- `requests` library
- Internet connection

## 💾 Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/naukri-scraper.git
cd naukri-scraper
```

2. Install the required dependencies:
```bash
pip install requests
```

## 🚀 Usage

1. Run the main script:
```bash
python SCRAPPER.py
```

2. Enter the job title you want to search for when prompted:
```
Enter the job title to search: Python Developer
```

3. Enter the page number to scrape:
```
Enter the page number: 1
```

4. The script will fetch job listings and save them to a CSV file named according to your search query.

## 📁 Project Structure

```
naukri-scraper/
├── SCRAPPER.py     # Main script for scraping job listings
├── headers.py      # Contains headers configuration for HTTP requests
├── cookies.py      # Contains cookies configuration for HTTP requests
└── README.md       # This documentation file
```

## 🔧 How It Works

1. The script sends an HTTP request to Naukri.com's API with your search query
2. It uses custom headers and cookies to simulate a browser session
3. The API response is parsed to extract job details
4. Job information is displayed in the terminal and saved to a CSV file
5. You can search for additional job titles or exit the program

## 📊 Sample Output

The script generates a CSV file with the following columns:
- Title
- Company
- Job Description
- Logo URL
- Experience
- Location
- Posted Date
- Salary
- Job ID
- Job URL
- Skills

## 👥 Contributing

Contributions are welcome! Feel free to submit pull requests or open issues to improve this project.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 🔗 Connect With Me

[![YouTube](https://img.shields.io/badge/YouTube-Channel-red?style=for-the-badge&logo=youtube)](https://www.youtube.com/@Pawankumar-py4tk)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/pawan941394/)
[![Instagram](https://img.shields.io/badge/Instagram-Profile-purple?style=for-the-badge&logo=instagram)](https://www.instagram.com/p_awan__kumar/)
[![Agency](https://img.shields.io/badge/Our_Agency-Contact_Us-orange?style=for-the-badge&logo=homeadvisor)](https://www.instagram.com/p_awan__kumar/)

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<p align="center">
  <i>Developed with ❤️ by <a href="https://www.youtube.com/@Pawankumar-py4tk">NbrainInf</a></i>
</p>
