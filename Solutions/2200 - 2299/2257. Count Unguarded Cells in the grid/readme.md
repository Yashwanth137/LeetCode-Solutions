### 1. Initialize the Matrix
```python
matrix = [[0 for _ in range(n)] for _ in range(m)]
```
- A 2D matrix of size \(m \times n\) is created, filled with `0`s.  
- This matrix represents the grid where:
  - `0` indicates unguarded cells.
  - `'G'` will indicate guard positions.
  - `'W'` will indicate wall positions.
  - `'P'` will indicate cells under the influence of guards.

---

### 2. Mark Guards in the Matrix
```python
for g in guards:
    matrix[g[0]][g[1]] = 'G'
```
- For each guard's coordinates \((x, y)\) in the `guards` list:
  - The matrix cell at \([x][y]\) is updated to `'G'` to mark the guard's position.

---

### 3. Mark Walls in the Matrix
```python
for w in walls:
    matrix[w[0]][w[1]] = 'W'
```
- For each wall's coordinates \((x, y)\) in the `walls` list:
  - The matrix cell at \([x][y]\) is updated to `'W'` to mark the wall's position.

---

### 4. Define Movement Directions
```python
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
```
- These represent the four cardinal directions:
  - \((-1, 0)\): Move up.
  - \((0, 1)\): Move right.
  - \((1, 0)\): Move down.
  - \((0, -1)\): Move left.

---

### 5. Mark Guard's Influence
```python
for g in guards:
    x, y = g
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        while 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] != 'G' and matrix[nx][ny] != 'W':
            matrix[nx][ny] = 'P'
            nx += dx
            ny += dy
```
- For each guard \((x, y)\):
  - Iterate through each direction \((dx, dy)\).
  - Propagate the guard's influence in that direction using a `while` loop:
    - Continue moving in the current direction until:
      - The boundary of the matrix is reached (\(nx, ny\) out of bounds).
      - A guard (`'G'`) or wall (`'W'`) blocks the path.
    - Mark the cell at \((nx, ny)\) as `'P'` (protected).
    - Update \((nx, ny)\) to the next cell in the current direction.

---

### 6. Count Unguarded Cells
```python
res = sum([1 for row in matrix for c in row if c == 0])
```
- Flatten the matrix and count all cells with value `0` (unguarded cells).  
- This is done using a generator expression:
  - For each row in the matrix, iterate through its cells.
  - Count cells where the value is `0`.

---

### 7. Return the Result
```python
return res
```
- The total number of unguarded cells (`res`) is returned.
