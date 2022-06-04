SLR_TABLE = {
    "ACCEPTED_STATES": {
        "T0": "",
        "T1": ""
    },
    "TRANSITION": {
        "T0": {"*": "T1"}
    }
}


class SyntaxAnalyzer:

    def __init__(self):
        self.table = {}  # Transition Table 초기화
        self.currentState = "T0"  # 처음 state를 T0로 선언
        self.finalStates = {}  # Final State 선언

    def SetTransitionTable(self, dfa):  # Transition Table 세팅
        self.table = dfa["TRANSITION"]
        self.finalStates.update(dfa["ACCEPTED_STATES"])

    def CheckNextState(self, _input):  # 다음 state를 check
        if not _input in self.table[self.currentState]:  # 만약 테이블 값에 없는 input 값이 들어오면 에러 반환 후 종료
            print("error")
            exit()
        nextState = self.table[self.currentState][_input]
        if nextState == "":  # 다음 state가 rejected 상태이면 "rejected" 반환
            return "rejected"
        else:  # 나머지 경우에는 nextState 반환
            return nextState

    def GetState(self):  # 현재 state를 알려줌
        return self.currentState

    def SetState(self, _state):
        self.currentState = _state

    def isFinalState(self):  # 현재 state가 final state인지 check
        if self.currentState in self.finalStates:
            return True
        else:
            return False

    def Reset(self):  # dfa reset
        self.currentState = "T0"


def main():
    dfa = SyntaxAnalyzer()
    dfa.SetTransitionTable(SLR_TABLE)
    inputString = "*"
    print(dfa.GetState())
    nextState = dfa.CheckNextState(inputString)
    dfa.SetState(nextState)
    print(dfa.GetState())
    if dfa.isFinalState():
        print("a")


if __name__ == "__main__":
    main()
