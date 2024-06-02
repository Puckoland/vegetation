import asyncio
from azure.servicebus.aio import ServiceBusClient
from azure.servicebus import ServiceBusMessage
import os

BUS_CONNECTION_STR = os.getenv('BUS_CONNECTION_STR')
QUEUE_NAME = "insertmessage"


async def send_single_message(sender, message: ServiceBusMessage):
    # Create a Service Bus message and send it to the queue
    await sender.send_messages(message)
    print("Sent a single message")


async def send_plant_async(plant):
    async with ServiceBusClient.from_connection_string(
            conn_str=BUS_CONNECTION_STR,
            logging_enable=True) as servicebus_client:
        sender = servicebus_client.get_queue_sender(queue_name=QUEUE_NAME)
        async with sender:
            message = ServiceBusMessage(str(plant))
            await send_single_message(sender, message)


def send_plant(plant):
    asyncio.run(send_plant_async(plant))
