from mercury.main import create_async_db, create_setting, create_starlette_app

setting = create_setting()
async_db = create_async_db(setting.mongo)
create_starlette_app(setting, async_db).launch()
