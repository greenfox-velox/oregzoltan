'use strict';
const isSudokuLineValid = require('./dojo');

var invalidFourTimesFourList = [
  [1, 3, 2, 4],
  [4, 3, 2, 1],
  [2, 1, 4, 3],
  [3, 4, 1, 2]]

  function getColumn(sudoku) {
    let columns = [
      [],
      [],
      [],
      []
    ];
    for (var r = 0; r < sudoku.length; r++) {
      for (var c = 0; c < sudoku.length; c++) {
        columns[c].push(sudoku[r][c]);
      }
    }
    return columns;
  }

function isSudokuValid(sudoku) {
  var sudokuColumns = getColumn(sudoku);
  return sudoku.every(isSudokuLineValid) && sudokuColumns.every(isSudokuLineValid);
}

module.exports = isSudokuValid;
