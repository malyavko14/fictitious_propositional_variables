# Fictitious propositional variables

## Software implementation
As part of the laboratory work, an algorithm was implemented using standard Python tools that allows you to list fictitious propositional variables 
in a formula of an abbreviated logic language. The essence of the algorithm is to translate the formula into a line of code that is understandable to 
the program, as well as to create a truth table for searching for fictitious propositional variables.

## Grammar of the Utterance logic language
* < constant > ::= 1|0 
* < symbol > ::= A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z
* < negation > ::= !
* < conjunction > ::= /\
* < disjunction > ::= \/
* < implication > ::= ->
* < disjunction > ::= \/
* < opening bracket > ::= (
* < closing bracket > ::= )
* < binary bundle > ::= < conjunction > | < disjunction > | < implication > | < equivalence >
* < atom > ::= < symbol >
* < unary complex formula > ::= < opening bracket > < negation > < formula > < closing bracket >
* < binary complex formula > ::= < opening bracket > < formula > < binary bundle > < formula > < closing bracket >
* < formula > ::= < constant > | < atom > | < unary complex formula > | < binary complex formula >

## Testing system
As part of the laboratory work, a system for testing the algorithm was implemented. The test consists of 14 tests.

## GUI
A simple interface was created that allows you to click on the “Check” button to display a dialog box with the result of checking the formula that is entered in the string.

<p align="center">
  <img src="https://user-images.githubusercontent.com/65425021/121747015-6686f280-cb0f-11eb-9f15-cf949c6b2816.png" />
</p>
