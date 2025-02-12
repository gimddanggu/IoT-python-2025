## 2025.02.12 단어추가기능
## 2025.02.13 UI 변경 및 단어 추가 후 엑셀파일 저장 기능
- 변경사항
    - 서브윈도우 생성
- 배운점
    - grid()랑 pack() 같이 사용 못 함
        - _tkinter.TclError: cannot use geometry manager grid inside . which already has slaves managed by pack
        
    - 메인윈도우 Tk() 서브 윈도우: Toplevel()
    - 파일 읽어올 때 unnamed: 0 column 생기는 오류 index_col=0 으로 해결

- 수정해야할 점
    - 인덱스 겹치는 문제
    - 단어입력 창 닫지 않고 다시 입력하면 중복으로 단어 입력됨
    - 단어 입력하면 엔트리 초기화하고 커서 단어 입력차으로 오도록
    - 저장 버튼 누르면 창 닫히게
    - ui 개선