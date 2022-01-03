# homelab-pi-stats

# Setup development environment
```sh
virtualenv venv
source venv/bin/activate.fish
pip install -r requirements.txt
```

# Environment vars
```env
# .env
ENV=local
```

# Local development
```sh
# Run on machine
python src/main.py

# Run on docker
earthly +compose-up
earthly +compose-down
```

# Release
```sh
earthly --build-arg TAG=<TAG> --push +release
```
