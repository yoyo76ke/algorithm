
#!/usr/bin/env python3

class Solution(object):
    """
    leetCode 937. Reorder Data in Log Files
    https://leetcode.com/problems/reorder-data-in-log-files/
    """
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        letLogs = [log for log in logs if log[-1].isalpha()]
        diglogs = [log for log in logs if log[-1].isdigit()]

        letRevLog = []
        for log in letLogs:
            print("log in letLogs is %d", log)
            sptlst = log.split()
            tmpRev = " ".join(sptlst[1:])+" "+ sptlst[0]
            letRevLog.append(tmpRev)
        sortedLet = sorted(letRevLog)

        actual = []
        for log in sortedLet:
            print("log in sortedLet is %d", log)
            sptlst = log.split()
            tmpLog = sptlst[-1]+" "+ sptlst[:-1]
            actual.append(tmpLog)
        
        return actual+diglogs