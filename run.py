#!/usr/bin/env python3
"""
License Plate Recognition System Runner
"""
import os
import sys
import subprocess
import argparse
from pathlib import Path

def install_dependencies():
    """Install required dependencies"""
    print("📦 Installing dependencies...")
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], check=True)
        print("✅ Dependencies installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing dependencies: {e}")
        sys.exit(1)

def setup_environment():
    """Setup environment files"""
    print("🔧 Setting up environment...")
    
    # Create .env file if it doesn't exist
    if not os.path.exists('.env'):
        if os.path.exists('env.example'):
            import shutil
            shutil.copy('env.example', '.env')
            print("✅ Created .env file from template")
        else:
            print("⚠️  No env.example found, please create .env manually")
    else:
        print("✅ .env file already exists")

def create_directories():
    """Create necessary directories"""
    print("📁 Creating directories...")
    
    directories = ['uploads', 'static/css', 'static/js', 'static/images', 'logs']
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"✅ Created directory: {directory}")

def run_development():
    """Run in development mode"""
    print("🚀 Starting License Plate Recognition System in development mode...")
    print("📍 Application will be available at: http://localhost:5000")
    print("🔍 Health check: http://localhost:5000/health")
    print("⏹️  Press Ctrl+C to stop the server")
    
    try:
        subprocess.run([sys.executable, "app.py"])
    except KeyboardInterrupt:
        print("\n👋 Server stopped by user")
    except Exception as e:
        print(f"❌ Error running application: {e}")

def run_production():
    """Run in production mode with Gunicorn"""
    print("🚀 Starting License Plate Recognition System in production mode...")
    
    try:
        subprocess.run([
            sys.executable, "-m", "gunicorn",
            "-w", "4",
            "-b", "0.0.0.0:5000",
            "--timeout", "120",
            "app:app"
        ])
    except KeyboardInterrupt:
        print("\n👋 Server stopped by user")
    except Exception as e:
        print(f"❌ Error running application: {e}")

def check_requirements():
    """Check if all requirements are met"""
    print("🔍 Checking requirements...")
    
    # Check Python version
    if sys.version_info < (3, 7):
        print("❌ Python 3.7+ is required")
        sys.exit(1)
    else:
        print(f"✅ Python {sys.version.split()[0]} detected")
    
    # Check if requirements.txt exists
    if not os.path.exists('requirements.txt'):
        print("❌ requirements.txt not found")
        sys.exit(1)
    else:
        print("✅ requirements.txt found")
    
    # Check if app.py exists
    if not os.path.exists('app.py'):
        print("❌ app.py not found")
        sys.exit(1)
    else:
        print("✅ app.py found")

def main():
    """Main function"""
    parser = argparse.ArgumentParser(description="License Plate Recognition System")
    parser.add_argument("command", choices=["install", "setup", "dev", "prod", "check"], 
                       help="Command to run")
    
    args = parser.parse_args()
    
    if args.command == "check":
        check_requirements()
    elif args.command == "install":
        check_requirements()
        install_dependencies()
    elif args.command == "setup":
        check_requirements()
        install_dependencies()
        setup_environment()
        create_directories()
        print("\n🎉 Setup complete! You can now run:")
        print("   python run.py dev    # Development mode")
        print("   python run.py prod   # Production mode")
    elif args.command == "dev":
        run_development()
    elif args.command == "prod":
        run_production()

if __name__ == "__main__":
    main()
