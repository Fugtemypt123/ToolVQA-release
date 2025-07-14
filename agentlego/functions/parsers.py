class GraphParser:
    def __init__(self):
        self.graph = None
        self.nodes = None
        self.edges = None
        self.edges_with_weight = None
        self.dfs_graph = None

    def __call__(self, graph):
        self.graph = graph
        self.nodes = graph[0]
        self.edges = graph[1]
        self.edges_with_weight = graph[2]
        self.dfs_graph = {('Start', -1): {'node':[], 'weight':[]}}
        for node in self.nodes:
            node = (node[0], node[1])
            self.dfs_graph[node] = {'node':[], 'weight':[]}
        for edge in self.edges_with_weight:
            edge[0] = (edge[0][0], edge[0][1])
            edge[1] = (edge[1][0], edge[1][1])
            self.dfs_graph[edge[0]]['node'].append(edge[1])
            self.dfs_graph[edge[0]]['weight'].append(edge[2])
        return self.dfs_graph

parse_graph = GraphParser()


class BaseParser:
    def __init__(self):
        pass

    def __call__(self, input, output):
        return self.template.format(result=output)
    

class CalculatorParser(BaseParser):
    def __init__(self):
        super().__init__()
        self.template = "The result of {expression} is {result}."

    def __call__(self, input, output):
        return self.template.format(expression=input['expression'], result=output)
    

class GoogleSearchParser(BaseParser):
    def __init__(self):
        super().__init__()
        self.template = "The search results for '{query}' are as follows:\n{result}"

    def __call__(self, input, output):
        # output = output.split('\n')[0] # 只取第一个结果不然废话太多
        return self.template.format(query=input['query'], result=output)
    

class PlotParser(BaseParser):
    def __init__(self):
        super().__init__()
        self.template = """You have used matplotlib to plot the graph of some data.
The plot code is as follows:
{command} 
And the plot result is saved in path '{result}'."""

    def __call__(self, input, output):
        return self.template.format(command=input['command'], result=output)


class SolverParser(BaseParser):
    def __init__(self):
        super().__init__()
        self.template = "The solution to the equation is {result}."


class OCRParser(BaseParser):
    def __init__(self):
        super().__init__()
        self.template = "The texts and their coordinates in the image are as follows:\n{result}"


class ImageDescriptionParser(BaseParser):
    def __init__(self):
        super().__init__()
        self.template = "{result}"


class TextToBboxParser(BaseParser):
    def __init__(self):
        super().__init__()
        self.template = "The '{object}' in the image is at {bbox}."

    def __call__(self, input, output):
        return self.template.format(object=input['text'], bbox=output)
    

class CountGivenObjectParser(BaseParser):
    def __init__(self):
        super().__init__()
        self.template = "The number of '{text}' in the image is {result}."

    def __call__(self, input, output):
        return self.template.format(text=input['text'], result=output)
    

class MathOCRParser(BaseParser):
    def __init__(self):
        super().__init__()
        self.template = "The mathematical expression in the image is {result}."

    def __call__(self, input, output):
        # {"request_id":"2024_09_08_3737a9f8fb0f155b91f3g","version":"RSK-M132p9","image_width":2585,"image_height":382,"is_printed":false,"is_handwritten":true,"auto_rotate_confidence":0,"auto_rotate_degrees":0,"confidence":0.99951171875,"confidence_rate":0.9999787654211914,"latex_styled":"\\left(\\frac{p 2^{-p}}{1+p}-1\\right)","text":"$\\left(\\frac{p 2^{-p}}{1+p}-1\\right)$"}
        text = output.split('"text":"')[1].split('"}')[0]
        return self.template.format(result=text)
    

class DrawBoxParser(BaseParser):
    def __init__(self):
        super().__init__()
        self.template = "The image with boxes '{bbox}' drawn is saved in path '{result}'."

    def __call__(self, input, output):
        return self.template.format(bbox=input['bbox'], result=output)


class AddTextParser(BaseParser):
    def __init__(self):
        super().__init__()
        self.template = "The image with text added is saved in path '{result}'."


class TextToImageParser(BaseParser):
    def __init__(self):
        super().__init__()
        self.template = "You have generated a picture that shows '{text}' and saved in path '{result}'."

    def __call__(self, input, output):
        return self.template.format(text=input['keywords'], result=output)
    

class ImageStylizationParser(BaseParser):
    def __init__(self):
        super().__init__()
        self.template = "The stylized image is saved in path '{result}'."


class RegionAttributeDescriptionParser(BaseParser):
    def __init__(self):
        super().__init__()
        self.template = "The attribute '{attribute}' of the region {region} is as follows:\n{result}"

    def __call__(self, input, output):
        return self.template.format(attribute=input['attribute'], region=input['bbox'], result=output)


parser_map = {
    'Calculator': CalculatorParser(),
    'GoogleSearch': GoogleSearchParser(),
    'Plot': PlotParser(),
    'Solver': SolverParser(),
    'OCR': OCRParser(),
    'ImageDescription': ImageDescriptionParser(),
    'TextToBbox': TextToBboxParser(),
    'CountGivenObject': CountGivenObjectParser(),
    'MathOCR': MathOCRParser(),
    'DrawBox': DrawBoxParser(),
    'AddText': AddTextParser(),
    'TextToImage': TextToImageParser(),
    'ImageStylization': ImageStylizationParser(),
    'RegionAttributeDescription': RegionAttributeDescriptionParser()
}