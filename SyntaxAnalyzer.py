SLR_TABLE = {
    "ACCEPTED_STATES": {
        "T1": "",
        "T2": "",
        "T3": "",
        "T4": "",
        "T5": "",
        "T6": "",
        "T7": "",
        "T8": "",
        "T9": ""
    },
    "TRANSITION": {
        "T1": {"*": "", "(": "S4", ")": "", "id": "S5", "$": "", "E": "2", "T": "3"},
        "T2": {"*": "", "(": "", ")": "", "id": "", "$": "R1", "E": "", "T": ""},
        "T3": {"*": "S6", "(": "", ")": "R3", "id": "", "$": "R3", "E": "", "T": ""},
        "T4": {"*": "", "(": "S4", ")": "", "id": "S5", "$": "", "E": "7", "T": "3"},
        "T5": {"*": "R5", "(": "", ")": "R5", "id": "", "$": "R5", "E": "", "T": ""},
        "T6": {"*": "", "(": "S4", ")": "", "id": "S5", "$": "", "E": "8", "T": "3"},
        "T7": {"*": "", "(": "", ")": "", "id": "", "$": "", "E": "", "T": ""},
        "T8": {"*": "", "(": "", ")": "", "id": "", "$": "R2", "E": "", "T": ""},
        "T9": {"*": "R4", "(": "", ")": "", "id": "", "$": "R4", "E": "", "T": ""}
    }
}

ReduceLengthList = [1, 3, 1, 3, 1]
ReduceStringList = ["S'", "E", "E", "T", "T"]


class SyntaxAnalyzer:

    def __init__(self):
        self.table = {}  # Transition Table 초기화
        self.currentState = "T1"  # 처음 state를 T0로 선언
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
        self.currentState = "T1"


def main():
    dfa = SyntaxAnalyzer()
    dfa.SetTransitionTable(SLR_TABLE)
    inputString = "id * id $"
    inputStringList = inputString.split()
    leftSubstring = []
    stack = [dfa.currentState]
    isAccepted = False
    while len(inputStringList) != 0:
        if dfa.CheckNextState(inputStringList[0])[0] == "S":
            stateNumber = dfa.CheckNextState(inputStringList[0])[1::]
            leftSubstring.append(inputStringList.pop(0))
            dfa.SetState("T" + str(stateNumber))
            stack.append(dfa.currentState)
        elif dfa.CheckNextState(inputStringList[0])[0] == "R":
            reduceIndex = dfa.CheckNextState(inputStringList[0])[1::]
            for k in range(ReduceLengthList[int(reduceIndex) - 1]):
                leftSubstring.pop()
                stack.pop()
            inputStringList.insert(0, ReduceStringList[int(reduceIndex) - 1])
            dfa.SetState(stack[-1])
            if inputStringList[0] == "S'":
                isAccepted = True
                break
        else:
            dfa.SetState("T" + dfa.CheckNextState(inputStringList[0]))
            leftSubstring.append(inputStringList.pop(0))
            stack.append(dfa.currentState)

    if isAccepted:
        print("ACCEPTED!")
    else:
        print("REJECTED!")


if __name__ == "__main__":
    main()
