def generate_pascal(num_rows):
  
  triangle = []
  for row_num in range(num_rows):
    current_row = [1] * (row_num + 1)
    for i in range(1, len(current_row) - 1):
      current_row[i] = triangle[row_num - 1][i - 1] + triangle[row_num - 1][i]
      
      triangle.append(current_row)
    
  return triangle

      
