class Solution:
    def quickSort(self, arr, low, high):
        if low < high:
            p_ind = self.partition(arr, low, high)
            self.quickSort(arr, low, p_ind - 1)
            self.quickSort(arr, p_ind + 1, high)
        return arr

    def partition(self, arr, low, high):
        pivot = arr[low]
        i, j = low, high

        while i < j:
            while arr[i] <= pivot and i <= high - 1:
                i += 1
            while arr[j] > pivot and j >= low + 1:
                j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]

        arr[j], arr[low] = arr[low], arr[j]
        return j