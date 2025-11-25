# Octave-Based Discord Bot

A Discord bot that allows users to execute [GNU Octave](https://octave.org/) code directly through Discord messages. Octave is an open-source numerical computing language highly compatible with MATLAB, making this bot a powerful calculator and scientific computing tool for Discord servers.

## Features

- Execute Octave/MATLAB code directly in Discord
- Support for mathematical operations, matrix calculations, and scientific functions
- Error handling with user-friendly messages

## Requirements

- **Python 3.8+**
- **GNU Octave** installed on the host system ([Download Octave](https://octave.org/download))
- A Discord Bot Token ([Discord Developer Portal](https://discord.com/developers/applications))

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/Octave-Based-Discord-Bot.git
   cd Octave-Based-Discord-Bot
   ```

2. **Install GNU Octave** (if not already installed)
   - Windows: Download from [octave.org](https://octave.org/download) and add to PATH
   - Linux: `sudo apt install octave`
   - macOS: `brew install octave`

3. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   cp example.env .env
   ```
   Edit `.env` and add your Discord bot token:
   ```
   TOKEN=your_bot_token_here
   ```

5. **Run the bot**
   ```bash
   python main.py
   ```

## Usage

Use the `!eval` command followed by any valid Octave/MATLAB code:

```
!eval 2 + 2
```
> 4

```
!eval sin(pi/2)
```
> 1

```
!eval A = [1 2; 3 4]; det(A)
```
> -2

```
!eval linspace(0, 10, 5)
```
> [0, 2.5, 5, 7.5, 10]

```
!eval factorial(10)
```
> 3628800

## Commands

| Command        | Description                 | Example           |
|----------------|-----------------------------|-------------------|
| `!eval <code>` | Evaluate Octave/MATLAB code | `!eval sqrt(144)` |

## Discord Bot Permissions

The bot requires the following permissions:
- Read Messages / View Channels
- Send Messages
- Read Message History

Make sure to enable the **Message Content Intent** in the Discord Developer Portal.

## TODO

> *This bot is currently in early development. Future improvements planned:*

- [ ] Add timeout protection for long-running computations
- [ ] Implement rate limiting to prevent abuse
- [ ] Add support for multi-line code blocks
- [ ] Create persistent user sessions with saved variables
- [ ] Add plotting support (save plots as images and send to Discord)
- [ ] Implement a `!help` command with Octave syntax examples
- [ ] Add code formatting for output (syntax highlighting)
- [ ] Support for uploading and executing `.m` files
- [ ] Add permission system (restrict usage to certain roles)
- [ ] Implement command cooldowns
- [ ] Add logging for debugging and usage analytics
- [ ] Sanitize/sandbox code execution for security
- [ ] Add support for symbolic math (if Octave symbolic package is installed)
- [ ] Create Docker container for easy deployment

## Tech Stack

- **[discord.py](https://discordpy.readthedocs.io/)** - Discord API wrapper
- **[oct2py](https://oct2py.readthedocs.io/)** - Python to Octave bridge
- **[python-dotenv](https://github.com/theskumar/python-dotenv)** - Environment variable management

## Project Structure

```
Octave-Based-Discord-Bot/
├── main.py           # Bot entry point and command handlers
├── requirements.txt  # Python dependencies
├── example.env       # Environment variable template
├── .env              # Your local config (git-ignored)
└── README.md         # This file
```

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.