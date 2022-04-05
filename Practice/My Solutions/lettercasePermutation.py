def letterCasePermutation(s):
        
        output = []
        currentIndex = 0
        length = len(s)

    
        def traverse(word, currIndex, sols):
            if currIndex == length:
                for sol in sols:
                    output.append(sol)
                return 

            elif isinstance(word[currIndex], int):
                currIndex += 1
                traverse(word, currIndex, sols)

            else:
                lengthSol = len(sols)-1
                for i in range(length):
                    print(currIndex)
                    sols.append(sols[i][currIndex].upper())
                    sols.append(sols[i][currIndex].lower())
                    print(sols)
                currIndex += 1
                traverse(word, currIndex, sols)
                
        
        traverse(s, currentIndex, [s])
        
        return output


print(letterCasePermutation("aBc"))