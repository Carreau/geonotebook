def _jupyter_server_extension_paths():
    return [{
        "module": "geonotebook"
    }]

def _jupyter_nbextension_paths():
    return [dict(
        section="notebook",
        src="static",
        # directory in the `nbextension/` namespace
        dest="geonotebook",
        # _also_ in the `nbextension/` namespace
        require="geonotebook/index")]



def load_jupyter_server_extension(nbapp):

    nbapp.log.info("geonotebook module enabled!")
#    nbapp.kernel.comm_manager.register_target('test', comm_opened)
