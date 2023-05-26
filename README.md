# BTQ Chat

<p align="left">
<img src="https://img.shields.io/github/languages/top/christopherlam888/btq-chat.svg" >
<a href="https://github.com/psf/black"><img src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
<img src="https://img.shields.io/badge/License-MIT-blue.svg">
</p>

A command-line interface for using ChatGPT via the BTQ Bot powered by Turbo 3.5.

## Features

- Quick and simple method to generate a response from a single prompt
- Use ChatGPT Turbo 3.5 privately and without an account

## Supported Site

- The Big Tech Question: <https://bigtechquestion.com/get-your-tech-problems-solved-by-the-btq-bot/>

## Installation

Clone/Download the GitHub repository:

```git clone https://github.com/christopherlam888/btq-chat.git```

Navigate to the directory:

```cd btq-chat```

Install requirements:

```pip3 install -r requirements.txt```

Chrono Crawler uses Selenium with the Chrome WebDriver. Install Chrome/Chromium before using.

## Usage

| **Command**                                   | **Description**                                                |
| :-------------------------------------------- | :------------------------------------------------------------- |
| `python3 -m btq_chat -p [prompt]`             | Run BTQ Chat with a specified prompt                           |
| `python3 -m chrono_crawler -h`                | Show help message.                                             |

## Features To Implement

- Enter multiple separate prompts
- Enter consecutive prompts with history

## License

This project is licensed under the MIT License.
