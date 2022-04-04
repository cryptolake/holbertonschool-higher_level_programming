#!/usr/bin/node
exports.addMeMaybe = (x, theFunction) => {
    theFunction(++x);
};
