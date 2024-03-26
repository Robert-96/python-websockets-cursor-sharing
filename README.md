# python-websockets-cursor-sharing

An WebSocket server for an interactive web application that shares cursor positions in real-time.

## Install

To get started, install the required dependencies using pip:

```console
pip install -r requirements.txt
```

## Development Setup

After installing the dependencies, run the following command to start the server:

```console
python server.py
```

By default, the server runs on port `7171`. To change the port, set the environment variable `WS_PORT`:

```console
export WS_PORT=7777
```

### Reload on code changes

During development, use ``watchmedo`` to automatically restart the server upon code changes. First, install the required tool:

```console
pip install -r requirements-dev.txt
```

Then, execute:

```console
watchmedo auto-restart --pattern "*.py" --recursive --signal SIGTERM python server.py
```

This command ensures that your server restarts whenever changes are made to Python files within the project directory.

## License

This project is licensed under the [MIT License](LICENSE).
