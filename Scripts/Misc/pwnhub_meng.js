function decode(path,dest,dest2){
	var flag = [];
	var relPosition = [],
	f1 = fs.readFileSync(path),
	d1 = fs.readFileSync(dest),
	d2 = fs.readFileSync(dest2),
	ff1 = new pp(f1),
	dd1 = new pp(d1),
	key = new pp(d2),
	picSize = ff1.size(),
	pixelNum = picSize.width*picSize.height;
	for (i = 0;i<picSize.height;i++)
		for(var j=0;j<picSize.width;j++)
		{
			var t1 = ff1.get(j,i);
			var t2 = dd1.get(j,i);
			if((t1.b-t2.b)!=0)
			{
				if((t1.r-t2.r)==0)
				{
					var k1 = key.get(j,i);
					flag[t2.g]=String.fromCharCode(k1.g);

				}
				else{
					var k1 = key.get(i,j);
					flag[k1.g]=String.fromCharCode(k1.b);
				}
			}
		}
		console.log(flag);

}
var pp = require('png-img'),
	fs = require('fs');
decode("1.png","dest.png","key.png");
