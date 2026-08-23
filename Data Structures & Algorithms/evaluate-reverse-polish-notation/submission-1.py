class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []

        for token in tokens:
            if token[0].isdigit() or (len(token) > 1 and token[0] == '-'):
                st.append(int(token))
            else:
                val1 = st.pop()
                val2 = st.pop()

                if token == '+':
                    st.append(val2 + val1)
                elif token == '-':
                    st.append(val2 - val1)
                elif token == '*':
                    st.append(val2 * val1)
                elif token == '/':
                    st.append(int(val2 / val1))

        return st.pop()