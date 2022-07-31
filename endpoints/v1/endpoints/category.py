from fastapi import APIRouter, HTTPException, Query

from schemas import BotUserSchema, BotUserInDBSchema
from crud_async import CRUDBotUser


bot_user_router = APIRouter(
    prefix="/bot_user"
)


@bot_user_router.get("/get", response_model=BotUserInDBSchema, tags=["BotUser"])
async def get_bot_user(bot_user_id: int = Query(ge=1)):
    bot_user = await CRUDBotUser.get(bot_user_id=bot_user_id)
    if bot_user:
        return bot_user
    else:
        raise HTTPException(status_code=404, detail=f"bot_user with id {bot_user_id} not found")

@bot_user_router.get("/all", response_model=list[BotUserInDBSchema], tags=["BotUser"])
async def get_all_bot_users(language_id: int = Query(ge=1)):
    bot_users = await CRUDBotUser.get_all(language_id=language_id)
    return bot_users


@bot_user_router.post("/add", response_model=BotUserInDBSchema, tags=["BotUser"])
async def add_bot_user(bot_user: BotUserSchema):
    bot_user = await CRUDBotUser.add(bot_user=bot_user)
    if bot_user:
        return bot_user
    else:
        raise HTTPException(status_code=404, detail="bot_user is exist")


@bot_user_router.delete("/del", tags=["BotUser"])
async def delete_bot_user(bot_user_id: int):
    await CRUDBotUser.delete(bot_user_id=bot_user_id)
    raise HTTPException(status_code=200, detail="bot_user was deleted")


@bot_user_router.put("/update", tags=["BotUser"])
async def update_bot_user(bot_user: BotUserInDBSchema):
    await CRUDBotUser.update(bot_user=bot_user)
    raise HTTPException(status_code=200, detail="bot_user was updated")
   # access_token = request.headers.get("Authorization")
   # if access_token:
      #  try:
      #      data = jwt.decode(access_token, CONFIG.AUTH.SECRET_KEY, algorithms=[CONFIG.AUTH.ALGORITHM])
     #   except JWTError:
      #      return False
       # username = data.get("sub")
       # if username:
          #  user = await CRUDUser.get_by_username(username=username)
           # if user:
            #    token_expire_date = data.get("exp")
             #   if token_expire_date:
            #        token_expire_date = datetime.utcfromtimestamp(token_expire_date)
           #         if datetime.utcnow() < token_expire_date:
          #              return True
         #           else:
        #                return False
       #         else:
      #              return False
     #       else:
    #            return False
   #     else:
  #          return False
 #   else:
     #   return False