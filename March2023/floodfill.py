from typing import List

def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    if image[sr][sc]==color:
        return image

    def dfs(image,sr,sc,color,oldColor):
        if sr<0 or sr>=len(image) or sc<0 or sc>=len(image[0]) or image[sr][sc]!=oldColor:
            return

        image[sr][sc]=color
        dfs(image,sr+1,sc,color,oldColor)
        dfs(image,sr-1,sc,color,oldColor)
        dfs(image,sr,sc+1,color,oldColor)
        dfs(image,sr,sc-1,color,oldColor)

    dfs(image,sr,sc,color,image[sr][sc])
    return image