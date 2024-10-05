# Pascal's Triangle
The Pascal's Triangle problem typically involves generating Pascal's Triangle up to a given number of rows.

Pascal's Triangle is a triangular array of numbers where:

- The first and last values in each row are always 1.
- Each interior value is the sum of the two values directly above it from the previous row.
    
#### Example:
```
       1
      1 1
     1 2 1
    1 3 3 1
   1 4 6 4 1
```

### Binomial Coefficients

Each number in Pascal's Triangle corresponds to the binomial coefficients. The value at row \(n\) and position \(k\) is given by:

$$
C(n, k) = \frac{n!}{k! \cdot (n - k)!}
$$
