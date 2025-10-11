# === Import libraries ===
import asyncio
import json
import websockets

# === Import packages ===
from websockets.exceptions import ConnectionClosed


# === Class 'SolScanner' ===
class SolScanner:
    """
    This class establishes and manages a WebSocket connection to the Solana blockchain's mainnet-beta
    endpoint for the purpose of real-time monitoring of transaction logs. It subscribes to all logs using
    the 'logsSubscribe' method with a 'processed' commitment level and continuously receives log data.
    The class is intended for developers, researchers, or systems that require streaming blockchain logs
    for analysis, alerting, or further processing. It uses asynchronous programming via Python’s asyncio
    and integrates the websockets library to handle the WebSocket lifecycle.

    Parameters:
    - url (str): A WebSocket URL to the Solana RPC node. Defaults to "wss://api.mainnet-beta.solana.com".

    Returns:
    - None
    """

    # === Function '__init__' ===
    def __init__(self, url="wss://api.mainnet-beta.solana.com"):
        """
        This initializer sets up a SolScanner instance by configuring the WebSocket endpoint URL
        that will be used for establishing a connection to the Solana blockchain. It prepares the scanner
        for subscribing to transaction log messages through a persistent WebSocket connection. The URL
        provided must point to a Solana-compatible RPC WebSocket endpoint that supports 'logsSubscribe'.

        Parameters:
        - url (str): WebSocket endpoint for Solana RPC (default is mainnet-beta WebSocket URL).

        Returns:
        - None
        """
        self.url = url

    # === Function 'run' ===
    async def run(self):
        """
        This function runs the main execution loop for the SolScanner instance. It establishes an
        asynchronous WebSocket connection, sends a JSON-formatted subscription request for all log messages,
        and enters an infinite loop to receive and parse each incoming message. Valid log messages are extracted
        from the response and printed line by line, with a visual separator. Error handling is implemented to
        catch malformed JSON and unexpected message formats, as well as connection closures and exceptions.

        Parameters:
        - None

        Returns:
        - None
        """
        try:
            async with websockets.connect(self.url) as ws:
                await ws.send(json.dumps({
                    "jsonrpc": "2.0",
                    "id": 1,
                    "method": "logsSubscribe",
                    "params": [
                        "all",
                        {"commitment": "processed"}
                    ]
                }))

                with open("solana.txt", "a", encoding="utf-8") as logfile:
                    while True:
                        message = await ws.recv()
                        try:
                            payload = json.loads(message)
                            logs = payload["params"]["result"]["value"]["logs"]
                            for line in logs:
                                print(line)
                                logfile.write(line + "\n")
                            print("-" * 80)
                            logfile.write("-" * 80 + "\n")

                        except json.JSONDecodeError:
                            print("Invalid JSON received.")
                            logfile.write("Invalid JSON received.\n")
                        except KeyError:
                            print("Missing keys in received data.")
                            logfile.write("Missing keys in received data.\n")
        except ConnectionClosed as e:
            print(f"WebSocket connection closed: {e}")
            with open("solana_logs.txt", "a", encoding="utf-8") as logfile:
                logfile.write(f"WebSocket connection closed: {e}\n")
        except Exception as e:
            print(f"Unexpected error: {type(e).__name__}: {e}")
            with open("solana_logs.txt", "a", encoding="utf-8") as logfile:
                logfile.write(f"Unexpected error: {type(e).__name__}: {e}\n")


# === Main Callback ===
if __name__ == "__main__":
    """
    This main entry point starts the SolScanner asynchronously when the script is executed directly.
    It initializes the event loop and runs the scanner’s main loop using asyncio. This allows the program
    to maintain a persistent WebSocket connection and continuously receive live log data from the Solana
    network. This part is crucial to bootstrap the asynchronous workflow of the scanner's real-time process.

    Parameters:
    - None

    Returns:
    - None
    """
    asyncio.run(SolScanner().run())
