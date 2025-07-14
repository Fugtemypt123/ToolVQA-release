DESCRIPTION_NEED = [
    'CountGivenObject',
    'TextToBbox',
    'ImageStylization',
]

# check if the tool need ImageDescription but it is not in the context
def check_tool(tools, image_path, name, now_context, generator_map):
    if name in DESCRIPTION_NEED:
        for d in now_context:
            if d['name'] == 'ImageDescription':
                return now_context
        tool = tools['ImageDescription']
        thought, input, output = generator_map['ImageDescription'](tool, image_path, now_context)
        now_context.append({
            'name': 'ImageDescription',
            'input': input,
            'output': output,
            'thought': thought,
        })
    return now_context 