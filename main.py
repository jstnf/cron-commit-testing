import json
import os
import time

def generate_output_folder() -> None:
  """
  Create the output folder if it does not already exist
  """
  if not os.path.isdir('generated'):
    os.mkdir('generated')

def main() -> None:
  """
  Perform the routine
  """
  generate_output_folder()

  current_time = round(time.time() * 1000)
  data = { "time": current_time }
  with open(f'generated/{current_time}.json', 'w') as f:
    f.write(f'{json.dumps(data)}')

if __name__ == '__main__':
  main()

# test