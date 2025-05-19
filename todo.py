if __name__ == "__main__":
    import os
    import sys
    import subprocess
    
    FLAG_FILE = ".requirements_installed"
    
    if not os.path.exists(FLAG_FILE):
        while True:
            answer = input("필수 패키지가 없습니다. 설치할까요? (Yy/Nn): ")
            if answer in ("Y", "y"):
                REQ_FILE = "requirements.txt"
                
                if os.path.exists(REQ_FILE):
                    subprocess.run([sys.executable, "-m", "pip", "install", "-r", REQ_FILE], check=True)
                    
                    with open(FLAG_FILE, "w") as f:
                        f.write("ok")
                        
                        
                break
            elif answer in ("N", "n"):
                print("To_Do 실행을 종료합니다")
                break
            else:
                print("다시 입력해주세요")
                continue
        
    
    from todo.main import main
    
    main()