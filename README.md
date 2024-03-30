# Chat Bot Application

This is a simple application for creating chat bots that can work both in Discord and Telegram.

## Installation

Ensure that the required parameters are specified in the `.env` file:

   - `TG_TOKEN`: Your Telegram bot token.
   - `DS_TOKEN`: Your Discord bot token.
   - `BOT_TYPE`: The type of bot you want to run (`discord` or `telegram`).


### Run without Makefile

Run the main file `main.py`:

```bash
python main.py
```

### Run with Makefile

Run the following command to check for the presence of the `.env` file and create it if it does not exist (make sure to replace placeholders with actual tokens):

```bash
make run
```

### Makefile Commands for Local Development
In addition to running the application, the Makefile provides the following commands for local development:

- `test`: Run tests using pytest.
- `isort`: Format import statements using isort.
- `mypy`: Type-check the code using mypy.
- `black`: Format code using black.
- `lint`: Isort & black check

## Project Structure

- `chat_transport.py`: contains classes for managing message transport.
- `business_logic.py`: contains classes and functions related to the business logic of your application.
- `main.py`: the entry point of your application, where bot initialization and startup are performed.
- `settings.py`: the application settings file, including bot configuration.
- `utils.py`: contains utility functions.
- `setup.py`: bot setup before start.
- `mappings.py`: token map.

