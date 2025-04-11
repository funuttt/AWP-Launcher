import subprocess
import os
import sys
from pathlib import Path

def find_roblox_player():
    """Try to find the Roblox player executable in common installation locations."""
    # Common paths where Roblox might be installed
    possible_paths = [
        Path(os.environ.get('LOCALAPPDATA', '')) / "Roblox" / "Versions",
        Path(os.environ.get('PROGRAMFILES', '')) / "Roblox" / "Versions",
        Path(os.environ.get('PROGRAMFILES(X86)', '')) / "Roblox" / "Versions",
    ]
    
    for base_path in possible_paths:
        if not base_path.exists():
            continue
            
        # Look through version folders
        for version_folder in base_path.iterdir():
            player_path = version_folder / "RobloxPlayerBeta.exe"
            if player_path.exists():
                return str(player_path)
    
    return None

def launch_roblox():
    """Launch Roblox player directly."""
    roblox_path = find_roblox_player()
    
    if not roblox_path:
        print("Error: Could not find RobloxPlayerBeta.exe")
        print("Please enter the full path to RobloxPlayerBeta.exe:")
        roblox_path = input("> ").strip('"')
        
        if not os.path.exists(roblox_path):
            print(f"Path not found: {roblox_path}")
            input("Press Enter to exit...")
            return False
    
    try:
        print(f"Launching Roblox from: {roblox_path}")
        subprocess.Popen([roblox_path])
        print("Roblox launched successfully!")
        return True
    except Exception as e:
        print(f"Error launching Roblox: {e}")
        input("Press Enter to exit...")
        return False

if __name__ == "__main__":
    print("=== Direct Roblox Launcher ===")
    print("Bypassing AWP and launching Roblox directly...")
    success = launch_roblox()
    
    if success:
        print("Done! You can close this window.")
        # Wait a bit before closing
        import time
        time.sleep(3)
