.. testsetup:: *

   import pwnlib
   from   pwnlib.context import context
   import threading, logging, time
   log = pwnlib.log.getLogger('pwnlib.context')


:mod:`pwnlib.context` --- Setting runtime variables
=====================================================

.. autodata:: pwnlib.context.context

.. autoclass:: pwnlib.context.ContextType
    :members:

.. autoclass:: pwnlib.context.Thread
