class Solution:    
    
    def findUnion(self, a, b):
        st=set()
        for i in range(len(a)):
            st.add(a[i])
        for i in range (len(b)):
            st.add(b[i])
        return len(st)
            
