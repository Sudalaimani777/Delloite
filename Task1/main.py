import json
import datetime
import unittest

def convertFromFormat1(jsonObject):
    # Implement this function
    parts = jsonObject['location'].split('/')
    return {
        "deviceID": jsonObject['deviceID'],
        "deviceType": jsonObject['deviceType'],
        "timestamp": jsonObject['timestamp'],
        "location": {
            "country": parts[0],
            "city": parts[1],
            "area": parts[2],
            "factory": parts[3],
            "section": parts[4]
        },
        "data": {
            "status": jsonObject['operationStatus'],
            "temperature": jsonObject['temp']
        }
    }

def convertFromFormat2(jsonObject):
    # Implement this function
    dt = datetime.datetime.strptime(jsonObject['timestamp'], "%Y-%m-%dT%H:%M:%S.%fZ")
    # Python 3.3+ supports this, or we can just use timestamp calculation.
    # To handle timestamp correctly:
    timestamp_ms = int(dt.replace(tzinfo=datetime.timezone.utc).timestamp() * 1000)
    
    return {
        "deviceID": jsonObject['device']['id'],
        "deviceType": jsonObject['device']['type'],
        "timestamp": timestamp_ms,
        "location": {
            "country": jsonObject['country'],
            "city": jsonObject['city'],
            "area": jsonObject['area'],
            "factory": jsonObject['factory'],
            "section": jsonObject['section']
        },
        "data": {
            "status": jsonObject['data']['status'],
            "temperature": jsonObject['data']['temperature']
        }
    }


class TestConversion(unittest.TestCase):
    def test_format1(self):
        with open('data-1.json') as f:
            data = json.load(f)
        result = convertFromFormat1(data)
        with open('data-result.json') as f:
            expected = json.load(f)
        self.assertEqual(result, expected)

    def test_format2(self):
        with open('data-2.json') as f:
            data = json.load(f)
        result = convertFromFormat2(data)
        with open('data-result.json') as f:
            expected = json.load(f)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
