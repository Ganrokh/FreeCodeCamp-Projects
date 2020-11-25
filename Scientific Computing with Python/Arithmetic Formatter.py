import re


def arithmetic_arranger(problems, answers=False):
    # Check for possible errors
    if len(problems) > 5:
        return 'Error: Too many problems.'
    for i in problems:
        if re.search(re.compile('[A-Za-z]'), i):
            return 'Error: Numbers must only contain digits.'
        if re.search(re.compile('[\*\/]'), i):
            return "Error: Operator must be '+' or '-'."

    equations = [problem.split() for problem in problems]

    for i in equations:
        for y in i:
            if len(y) > 4:
                return 'Error: Numbers cannot be more than four digits.'

    # Add answers to each equation if required
    if answers:
        for i in equations:
            if i[1] == '+':
                i.append(str(int(i[0]) + int(i[2])))
            else:
                i.append(str(int(i[0]) - int(i[2])))

    ans = '' # Start building the answer

    # Format first numbers
    for i in equations:
        ans += '  ' + ' ' * (len(i[2]) - len(i[0])) + i[0] + '    '
    ans = ans[:-4] + '\n'

    # Format operator and second number
    for i in equations:
        ans += i[1] + ' ' + ' ' * (len(i[0]) - len(i[2])) + i[2] + '    '
    ans = ans[:-4] + '\n'

    # Add dashed lines below
    dashes = []  # Tracks number of dashes for each equation for future use
    for n, i in enumerate(equations):
        dashes.append(
            len(i[1] + ' ' + ' ' * (len(i[0]) - len(i[2]))) + len(i[2]))
        ans += '-' * dashes[n] + '    '
    ans = ans[:-4]

    # Add answers if applicable
    if answers:
        ans += '\n'
        for n, i in enumerate(equations):
            ans += ' ' * (dashes[n] - len(i[3])) + i[3] + '    '
        ans = ans[:-4]

    return ans