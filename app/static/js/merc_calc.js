/*
 * merc_calc.js
 * Copyright (C) 2014 mlckq <moon5ckq@gmail.com>
 *
 * Distributed under terms of the MIT license.
 */
function max_lv(rarity) {
    return 20 + rarity * 10;
}
function max_rouse_lv(rarity) {
    return 20 + rarity * 10 + 15 * 5;
}
function get_grow(value, dev_type, lv, rarity) {
    var sqr = function(x) {return x*x;}
    var min = function(x,y) {return x<y?x:y}
    var max = function(x,y) {return x>y?x:y}

    var ret = 0, ty = 0;
    var maxlv = max_lv(rarity);
    if (dev_type == "早熟") {
        ret = Math.floor(value + value * 0.9 * sqr((min(lv, maxlv) - 1) / (maxlv - 1)));
        ty = 1;
    } else if (dev_type == "平均") {
        ret = Math.floor(value + value * (min(lv, maxlv) - 1) / (maxlv - 1));
        ty = 2;
    } else {
        var a = (min(lv, maxlv) - 1) / (maxlv - 1);
        ret = Math.floor(value + value * 1.1 * Math.pow(a, 1.6));
        ty = 3;
    }

    if (lv > maxlv) {
        ret = ret + Math.floor(value / (maxlv - 1) * (0.8 + 0.1 * ty)) * (lv - maxlv);
    }

    return ret;
}
