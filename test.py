import unittest
from dummy_propositional_variables_in_formula import result as res


class Test(unittest.TestCase):

    def test1(self):
        formula = '(A/\(!A))'
        result = res(formula)
        self.assertEqual(result, "Fictitious propositional variables: ['A']")

    def test2(self):
        formula = '(B\/(!B))'
        result = res(formula)
        self.assertEqual(result, "Fictitious propositional variables: ['B']")

    def test3(self):
        formula = '(C~(!C))'
        result = res(formula)
        self.assertEqual(result, "Fictitious propositional variables: ['C']")

    def test4(self):
        formula = '(C~(!X))'
        result = res(formula)
        self.assertEqual(result, 'There are no fictitious propositional variables in this formula')

    def test5(self):
        formula = '((!A)~(B/\(!((!C)->D))))'
        result = res(formula)
        self.assertEqual(result, 'There are no fictitious propositional variables in this formula')

    def test6(self):
        formula = '(A->(!A))'
        result = res(formula)
        self.assertEqual(result, 'There are no fictitious propositional variables in this formula')

    def test7(self):
        formula = '(C->(!C))'
        result = res(formula)
        self.assertEqual(result, 'There are no fictitious propositional variables in this formula')

    def test8(self):
        formula = '(A->(C~(!D)))'
        result = res(formula)
        self.assertEqual(result, 'There are no fictitious propositional variables in this formula')

    def test9(self):
        formula = '(A\/(B->(C~D)))'
        result = res(formula)
        self.assertEqual(result, 'There are no fictitious propositional variables in this formula')

    def test10(self):
        formula = '(((P\/Q)->R)->((P\/R)->(Q\/R)))'
        result = res(formula)
        self.assertEqual(result, "Fictitious propositional variables: ['P', 'Q', 'R']")

    def test11(self):
        formula = '((A/\(B~C))~(!(A/\(B~C))))'
        result = res(formula)
        self.assertEqual(result, "Fictitious propositional variables: ['A', 'B', 'C']")

    def test12(self):
        formula = '((A/\(B~C))~(A/\(B~C)))'
        result = res(formula)
        self.assertEqual(result, "Fictitious propositional variables: ['A', 'B', 'C']")

    def test13(self):
        formula = '(A~(!(B\/(C/\\0)))'
        result = res(formula)
        self.assertEqual(result, "Check that the formula is correct")

    def test14(self):
        formula = '(A/\(B/\(C/\(D/\(E/\(F/\(G/\(H/\(I/\(J/\(K/\(L/\(M/\(N/\(O/\(P/\(Q/\(R/\(S/\(T/\(U/\(V/\(W/\(X/\(Y/\Z)))))))))))))))))))))))))'
        result = res(formula)
        self.assertEqual(result, "Fictitious propositional variables: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']")


if __name__ == '__main__':
    unittest.main()
