#!/usr/bin/env python3
"""
Crypto Signal Bot v5 — KOMBAJN DO RYNKU
Root entrypoint — delegates to core.bot

Usage:
  python bot.py --test --scan
  python bot.py --webhook URL --strategy nwo_stoch_cvd
  python bot.py --config aggressive --glm-key KEY
  python bot.py --market both --symbols BTC/USDT,XAU/USD,SP500
  python bot.py --api  # Start with REST API
"""

import sys
import os

# Add project root to path so package imports work
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from core.bot import main

if __name__ == "__main__":
    main()
