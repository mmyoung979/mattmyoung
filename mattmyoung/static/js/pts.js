Pts.namespace( window );

function floatySpace() {

  var space = new CanvasSpace("#pt").setup({ bgcolor: "#222222", retina: true, resize: true });
  var form = space.getForm();

  space.add( {
    start: (bound) => {},

    animate: (time, ftime) => {
      form.point( space.pointer, 10 );
    },

    action: (type, x, y) => {}
  });

  space.bindMouse().bindTouch().play();

};

floatySpace();
