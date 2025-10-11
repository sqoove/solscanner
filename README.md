# SolScanner - Python Based Solana Live Log Streamer

**SolScanner** powerfull real-time WebSocket-based log monitoring tool for the Solana blockchain. Solana Scanner allows developers, researchers, and blockchain enthusiasts to connect directly to Solana’s mainnet-beta WebSocket endpoint and stream all processed transaction logs. Built with Python’s `asyncio` and `websockets`, it offers a lightweight and extensible way to observe network activity and extract insights in real time.

* * *

## Features

- Connects to Solana mainnet-beta via WebSocket
- Subscribes to `logsSubscribe` with "processed" commitment
- Streams and prints logs from all transactions in real time
- Asynchronous and non-blocking using `asyncio`
- Simple and easily extensible Python codebase

* * *

## Use Cases

- Blockchain activity monitoring
- Security auditing and on-chain analysis
- Real-time developer debugging
- Building analytics dashboards or bots

* * *

## Installation

### Prerequisites

- Python 3.8+
- pip

### Install dependencies

```bash
pip install websockets
````

* * *

## Usage

Run the scanner with the default Solana mainnet WebSocket URL:

```bash
python solana_scanner.py
```

Or specify a custom Solana RPC WebSocket endpoint:

```python
scanner = SolanaScanner(url="wss://your-solana-rpc-websocket-url")
asyncio.run(scanner.run())
```

* * *

### File Structure

```
solana_scanner.py    # Main script for scanning Solana logs
```

* * *

### Example Output

```
Program 11111111111111111111111111111111 invoke [1]
Program 11111111111111111111111111111111 success
--------------------------------------------------------------------------------
```

* * *

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes and commit them (`git commit -m "Add your feature"`).
4. Push to your branch (`git push origin feature/your-feature`).
5. Open a pull request with a clear description of your changes.

Ensure your code follows PEP 8 style guidelines and includes appropriate tests.

* * *

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

* * *

## Contact

For any issues, suggestions, or questions regarding the project, please open a new issue on the official GitHub repository or reach out directly to the maintainer through the [GitHub Issues](issues) page for further assistance and follow-up.