#!/usr/bin/node
const axios = require('axios');

axios.get(process.argv[2])
  .then(resp => {
    const todos = resp.data;
    const completed = {};
    for (let i = 0; i < todos.length; i++) {
      if (todos[i].completed) {
        if (completed[todos[i].userId] !== undefined) {
          completed[todos[i].userId] += 1;
        } else {
          completed[todos[i].userId] = 1;
        }
      }
    }
    console.log(completed);
  });
