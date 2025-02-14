import json
import csv
import xml.etree.ElementTree as ET
import yaml

def json_to_dict(json_file):
    with open(json_file, 'r') as file:
        return json.load(file)

def dict_to_json(dictionary):
    return json.dumps(dictionary, indent=4)

def csv_to_dict(csv_file):
    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        return [row for row in reader]

def dict_to_csv(dictionary_list):
    if dictionary_list:
        output = []
        fieldnames = dictionary_list[0].keys()
        output.append(','.join(fieldnames))
        for row in dictionary_list:
            output.append(','.join(row.values()))
        return '\n'.join(output)
    return ""

def xml_to_dict(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    def parse_element(element):
        parsed_data = {}
        for child in element:
            parsed_data[child.tag] = parse_element(child) if len(child) else child.text
        return parsed_data

    return {root.tag: parse_element(root)}

def dict_to_xml(dictionary):
    def build_element(element, data):
        for key, value in data.items():
            child = ET.SubElement(element, key)
            if isinstance(value, dict):
                build_element(child, value)
            else:
                child.text = str(value)
    root_key = list(dictionary.keys())[0]
    root_value = dictionary[root_key]
    root = ET.Element(root_key)
    build_element(root, root_value)
    return ET.tostring(root, encoding='unicode')

def yaml_to_dict(yaml_file):
    with open(yaml_file, 'r') as file:
        return yaml.safe_load(file)

def dict_to_yaml(dictionary):
    return yaml.dump(dictionary, default_flow_style=False)

def json_to_yaml(json_file, yaml_file):
    dictionary = json_to_dict(json_file)
    yaml_data = dict_to_yaml(dictionary)
    with open(yaml_file, 'w') as file:
        file.write(yaml_data)

def yaml_to_json(yaml_file, json_file):
    dictionary = yaml_to_dict(yaml_file)
    json_data = dict_to_json(dictionary)
    with open(json_file, 'w') as file:
        file.write(json_data)

def main():
    while True:
        print(" 1  JSON to Dictionary")
        print(" 2  Dictionary to JSON")
        print(" 3  CSV to Dictionary")
        print(" 4  Dictionary to CSV")
        print(" 5  XML to Dictionary")
        print(" 6  Dictionary to XML")
        print(" 7  YAML to Dictionary")
        print(" 8  Dictionary to YAML")
        print(" 9  JSON to YAML")
        print(" 10 YAML to JSON")
        print(" 11 Programm beenden")

        choice = int(input("Wähle eine Konvertierung: "))

        if choice == 1:
            json_dict = json_to_dict('1.json')
            print("JSON to Dictionary:\n", json_dict)
        elif choice == 2:
            json_dict = json_to_dict('1.json')
            print("Dictionary to JSON:\n", dict_to_json(json_dict))
        elif choice == 3:
            csv_dict = csv_to_dict('2.csv')
            print("CSV to Dictionary:\n", csv_dict)
        elif choice == 4:
            csv_dict = csv_to_dict('2.csv')
            print("Dictionary to CSV:\n", dict_to_csv(csv_dict))
        elif choice == 5:
            xml_dict = xml_to_dict('3.xml')
            print("XML to Dictionary:\n", xml_dict)
        elif choice == 6:
            xml_dict = xml_to_dict('3.xml')
            print("Dictionary to XML:\n", dict_to_xml(xml_dict))
        elif choice == 7:
            yaml_dict = yaml_to_dict('4.yml')
            print("YAML to Dictionary:\n", yaml_dict)
        elif choice == 8:
            yaml_dict = yaml_to_dict('4.yml')
            print("Dictionary to YAML:\n", dict_to_yaml(yaml_dict))
        elif choice == 9:
            json_to_yaml('1.json', 'output.yaml')
            print("JSON to YAML konvertiert.")
        elif choice == 10:
            yaml_to_json('4.yml', 'output.json')
            print("YAML to JSON konvertiert.")
        elif choice == 11:
            print("Programm beendet.")
            break
        else:
            print("Ungültige Auswahl")

if __name__ == "__main__":
    main()
