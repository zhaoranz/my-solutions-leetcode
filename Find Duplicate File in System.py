class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_dict = collections.defaultdict(list)
        for i in paths:
            parts = i.split(" ")
            path = parts[0]
            for j in range(1, len(parts)):
                name_content = parts[j].split("(")
                file_name = name_content[0]
                content = name_content[1][:-1]
                content_dict[content].append(path+'/'+file_name)
        return [i for i in content_dict.values() if len(i)>1]
        
