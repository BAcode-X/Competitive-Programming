Array.prototype.last = function() {
    if(!this.length){
        return -1
    }
    return this.pop()
};
