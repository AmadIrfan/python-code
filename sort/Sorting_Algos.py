import Sorting_BL
import Sorting_Dl
from Sorting_Dl import Load_Data

def SelectionSort(method, Arr):
    for x in range(0, 6):
        if method == "Ascending":
            for i in range(0, len(Arr)):
                Min_Ind = i
                j = i+1
                for j in range(i+1, len(Arr)):
                    if str(Arr[j]) < str(Arr[Min_Ind]):
                        Min_Ind = j
                (Arr[i], Arr[Min_Ind]) = (Arr[Min_Ind], Arr[i])
                (Sorting_Dl.Mega_List[i], Sorting_Dl.Mega_List[Min_Ind]) = (
                    Sorting_Dl.Mega_List[Min_Ind], Sorting_Dl.Mega_List[i])
            return Arr
        if method == "Descending":
            for i in range(0, len(Arr)):
                Min_Ind = i
                j = i+1
                for j in range(i+1, len(Arr)):
                    if str(Arr[j]) > str(Arr[Min_Ind]):
                        Min_Ind = j
                (Arr[i], Arr[Min_Ind]) = (Arr[Min_Ind], Arr[i])
                (Sorting_Dl.Mega_List[i], Sorting_Dl.Mega_List[Min_Ind]) = (
                    Sorting_Dl.Mega_List[Min_Ind], Sorting_Dl.Mega_List[i])
            return Arr

def BubbleSort(method, Arr):
    if method == "Ascending":
        for i in range(0, len(Arr)):
            j = i+1
            for j in range(0, len(Arr)):
                if str(Arr[i]) < str(Arr[j]):
                    Temp_Val = Arr[i]
                    Arr[i] = Arr[j]
                    Arr[j] = Temp_Val
                    temp = Sorting_Dl.Mega_List[i]
                    Sorting_Dl.Mega_List[i] = Sorting_Dl.Mega_List[j]
                    Sorting_Dl.Mega_List[j] = temp
        return Arr
    if method == "Descending":
        for i in range(0, len(Arr)):
            j = i+1
            for j in range(0, len(Arr)):
                if str(Arr[i]) > str(Arr[j]):
                    Temp_Val = Arr[i]
                    Arr[i] = Arr[j]
                    Arr[j] = Temp_Val
                    temp = Sorting_Dl.Mega_List[i]
                    Sorting_Dl.Mega_List[i] = Sorting_Dl.Mega_List[j]
                    Sorting_Dl.Mega_List[j] = temp
        return Arr

def gnomeSort(method, Arr):
    if method == "Ascending":
        Index_Val = 0
        while Index_Val < len(Arr):
            if Index_Val == 0:
                Index_Val = Index_Val + 1
            if str(Arr[Index_Val]) >= str(Arr[Index_Val - 1]):
                Index_Val = Index_Val + 1
            else:
                Arr[Index_Val], Arr[Index_Val-1] = Arr[Index_Val-1], Arr[Index_Val]
                Sorting_Dl.Mega_List[Index_Val], Sorting_Dl.Mega_List[Index_Val -1] = Sorting_Dl.Mega_List[Index_Val-1], Sorting_Dl.Mega_List[Index_Val]
                Index_Val = Index_Val - 1

        return Arr
    if method == "Descending":
        Index_Val = 0
        while Index_Val < len(Arr):
            if Index_Val == 0:
                Index_Val = Index_Val + 1
            if str(Arr[Index_Val]) <= str(Arr[Index_Val - 1]):
                Index_Val = Index_Val + 1
            else:
                Arr[Index_Val], Arr[Index_Val-1] = Arr[Index_Val-1], Arr[Index_Val]
                Sorting_Dl.Mega_List[Index_Val], Sorting_Dl.Mega_List[Index_Val -
                                                                1] = Sorting_Dl.Mega_List[Index_Val-1], Sorting_Dl.Mega_List[Index_Val]
                Index_Val = Index_Val - 1

        return Arr

def shellSort(method, Arr):
    if method == "Ascending":
        n = len(Arr)
        Gap_Val = n//2
        while Gap_Val > 0:
            j = Gap_Val
            while j < n:
                i = j-Gap_Val
                while i >= 0:
                    if str(Arr[i+Gap_Val]) > str(Arr[i]):
                        break
                    else:
                        Arr[i+Gap_Val], Arr[i] = Arr[i], Arr[i+Gap_Val]
                        Sorting_Dl.Mega_List[i +Gap_Val], Sorting_Dl.Mega_List[i] = Sorting_Dl.Mega_List[i], Sorting_Dl.Mega_List[i+Gap_Val]
                    i = i-Gap_Val
                j += 1
            Gap_Val = Gap_Val//2
    if method == "Descending":
        n = len(Arr)
        Gap_Val = n//2
        while Gap_Val > 0:
            j = Gap_Val
            while j < n:
                i = j-Gap_Val
                while i >= 0:
                    if str(Arr[i+Gap_Val]) < str(Arr[i]):
                        break
                    else:
                        Arr[i+Gap_Val], Arr[i] = Arr[i], Arr[i+Gap_Val]
                        Sorting_Dl.Mega_List[i +
                                            Gap_Val], Sorting_Dl.Mega_List[i] = Sorting_Dl.Mega_List[i], Sorting_Dl.Mega_List[i+Gap_Val]
                    i = i-Gap_Val
                j += 1
            Gap_Val = Gap_Val//2