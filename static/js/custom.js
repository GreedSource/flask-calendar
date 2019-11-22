window.ParsleyValidator.setLocale('es');
function validarFormulario(f,objEsp){
	//	f: Objeto formulario (form)
	//	objEsp: Indica si se debe validar algún objeto no soportado por la librería Parsley.js
	var objEsp = objEsp || true;
	var expreg = /_$/;
	var resp = false;

	if(objEsp){
		for (i=0; i<f.elements.length; i++){
			objeto = f.elements[i];
			if(expreg.test(objeto.id)){
				//CKEditor
				var patron = /ckeditor/g;
				if(patron.test(objeto.className)){
					$("#"+objeto.id).val(CKEDITOR.instances[objeto.id].getData());
				}
			}
		}
	}

	resp = $("#"+f.id).parsley().validate();

	return resp;
}

function soloNumeros(e,decReq) {
	var key = (isIE) ? event.keyCode : e.which;
	var obj = (isIE) ? event.srcElement : e.target;
	var isNum = (key > 47 && key < 58) ? true : false;
	var dotOK = (key==46 && decReq=='decOK' && (obj.value.indexOf(".")<0 || obj.value.length==0)) ? true:false;
	var isDel = (key==0 || key==8 ) ? true:false;
	var isEnter = (key==13) ? true:false;
	//e.which = (!isNum && !dotOK && isNS) ? 0 : key;
	return (isNum || dotOK || isDel || isEnter);
}