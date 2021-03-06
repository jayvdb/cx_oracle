.. _connobj:

*****************
Connection Object
*****************

.. note::

   Any outstanding changes will be rolled back when the connection object
   is destroyed or closed.



.. method:: Connection.__enter__()

   The entry point for the connection as a context manager, a feature available
   in Python 2.5 and higher. It returns itself.

   .. note::

      This method is an extension to the DB API definition.


.. method:: Connection.__exit__()

   The exit point for the connection as a context manager, a feature available
   in Python 2.5 and higher. In the event of an exception, the transaction is
   rolled back; otherwise, the transaction is committed.

   .. note::

      This method is an extension to the DB API definition.


.. attribute:: Connection.action

   This write-only attribute sets the action column in the v$session table and
   is only available in Oracle 10g. It is a string attribute and cannot be set
   to None -- use the empty string instead.

   .. note::

      This attribute is an extension to the DB API definition.


.. attribute:: Connection.autocommit

   This read-write attribute determines whether autocommit mode is on or off.

   .. note::

      This attribute is an extension to the DB API definition.


.. method:: Connection.begin()
              Connection.begin([formatId, transactionId, branchId])

   Explicitly begin a new transaction. Without parameters, this explicitly
   begins a local transaction; otherwise, this explicitly begins a distributed
   (global) transaction with the given parameters. See the Oracle documentation
   for more details.

   Note that in order to make use of global (distributed) transactions, the
   twophase argument to the Connection constructor must be a true value. See
   the comments on the Connection constructor for more information
   (:ref:`module`).

   .. note::

      This method is an extension to the DB API definition.


.. method:: Connection.cancel()

   Cancel a long-running transaction.

   .. note::

      This method is an extension to the DB API definition.


.. method:: Connection.changepassword(oldpassword, newpassword)

   Change the password of the logon.

   .. note::

      This method is an extension to the DB API definition.


.. attribute:: Connection.client_identifier

   This write-only attribute sets the client_identifier column in the
   v$session table.

   .. note::

      This attribute is an extension to the DB API definition.


.. attribute:: Connection.clientinfo

   This write-only attribute sets the client_info column in the v$session table
   and is only available in Oracle 10g.

   .. note::

      This attribute is an extension to the DB API definition.


.. method:: Connection.close()

   Close the connection now, rather than whenever __del__ is called. The
   connection will be unusable from this point forward; an Error exception will
   be raised if any operation is attempted with the connection. The same
   applies to any cursor objects trying to use the connection.


.. method:: Connection.commit()

   Commit any pending transactions to the database.


.. attribute:: Connection.current_schema

   This read-write attribute sets the current schema attribute for the session.

   .. note::

      This attribute is an extension to the DB API definition.


.. method:: Connection.cursor()

   Return a new Cursor object (:ref:`cursorobj`) using the connection.


.. method:: Connection.deq(name, options, msgproperties, payload)

   Returns a message id after successfully dequeuing a message. The options
   object can be created using :meth:`~Connection.deqoptions()` and the
   msgproperties object can be created using
   :meth:`~Connection.msgproperties()`. The payload must be an object created
   using :meth:`~ObjectType.newobject()`.

   .. versionadded:: development

   .. note::

         This method is an extension to the DB API definition.


.. method:: Connection.deqoptions()

   Returns an object specifying the options to use when dequeuing messages.
   See :ref:`deqoptions` for more information.

   .. versionadded:: development

   .. note::

         This method is an extension to the DB API definition.


.. attribute:: Connection.dsn

   This read-only attribute returns the TNS entry of the database to which a
   connection has been established.

   .. note::

      This attribute is an extension to the DB API definition.


.. attribute:: Connection.edition

   This read-only attribute gets the session edition and is only available in
   Oracle Database 11.2 (both client and server must be at this level or higher
   for this to work).

   .. versionadded:: development

   .. note::

      This attribute is an extension to the DB API definition.


.. attribute:: Connection.encoding

   This read-only attribute returns the IANA character set name of the
   character set in use by the Oracle client.

   .. note::

      This attribute is an extension to the DB API definition and is only
      available in Python 2.x when not built in unicode mode.


.. method:: Connection.enq(name, options, msgproperties, payload)

   Returns a message id after successfully enqueuing a message. The options
   object can be created using :meth:`~Connection.enqoptions()` and the
   msgproperties object can be created using
   :meth:`~Connection.msgproperties()`. The payload must be an object created
   using :meth:`~ObjectType.newobject()`.

   .. versionadded:: development

   .. note::

         This method is an extension to the DB API definition.


.. method:: Connection.enqoptions()

   Returns an object specifying the options to use when enqueuing messages.
   See :ref:`enqoptions` for more information.

   .. versionadded:: development

   .. note::

         This method is an extension to the DB API definition.


.. method:: Connection.gettype(name)

   Return a type object (:ref:`objecttype`) given its name. This can then be
   used to create objects which can be bound to cursors created by this
   connection.

   .. versionadded:: development

   .. note::

         This method is an extension to the DB API definition.


.. attribute:: Connection.inputtypehandler

   This read-write attribute specifies a method called for each value that is
   bound to a statement executed on any cursor associated with this connection.
   The method signature is handler(cursor, value, arraysize) and the return
   value is expected to be a variable object or None in which case a default
   variable object will be created. If this attribute is None, the default
   behavior will take place for all values bound to statements.

   .. note::

      This attribute is an extension to the DB API definition.


.. attribute:: Connection.ltxid

   This read-only attribute returns the logical transaction id for the
   connection. It is used within Oracle Transaction Guard as a means of
   ensuring that transactions are not duplicated. See the Oracle documentation
   and the provided sample for more information.

   .. versionadded:: development

   .. note:

      This attribute is an extension to the DB API definition. It is only
      available when Oracle Database 12.1 or higher is in use on both the
      server and the client.


.. attribute:: Connection.maxBytesPerCharacter

   This read-only attribute returns the maximum number of bytes each character
   can use for the client character set.

   .. note::

      This attribute is an extension to the DB API definition.


.. attribute:: Connection.module

   This write-only attribute sets the module column in the v$session table and
   is only available in Oracle 10g. The maximum length for this string is 48
   and if you exceed this length you will get ORA-24960.

   .. note:

      This attribute is an extension to the DB API definition.


.. method:: Connection.msgproperties()

   Returns an object specifying the properties of messages used in advanced
   queuing. See :ref:`msgproperties` for more information.

   .. versionadded:: development

   .. note::

         This method is an extension to the DB API definition.


.. attribute:: Connection.nencoding

   This read-only attribute returns the IANA character set name of the national
   character set in use by the Oracle client.

   .. note::

      This attribute is an extension to the DB API definition and is only
      available in Python 2.x when not built in unicode mode.


.. attribute:: Connection.outputtypehandler

   This read-write attribute specifies a method called for each value that is
   to be fetched from any cursor associated with this connection. The method
   signature is handler(cursor, name, defaultType, length, precision, scale)
   and the return value is expected to be a variable object or None in which
   case a default variable object will be created. If this attribute is None,
   the default behavior will take place for all values fetched from cursors.

   .. note::

      This attribute is an extension to the DB API definition.


.. method:: Connection.ping()

   Ping the server which can be used to test if the connection is still active.

   .. note::

         This method is an extension to the DB API definition and is only
         available in Oracle 10g R2 and higher.


.. method:: Connection.prepare()

   Prepare the distributed (global) transaction for commit. Return a boolean
   indicating if a transaction was actually prepared in order to avoid the
   error ORA-24756 (transaction does not exist).

   .. note::

         This method is an extension to the DB API definition.


.. method:: Connection.register(code, when, function)

   Register the function as an OCI callback. The code is one of the function
   codes defined in the Oracle documentation of which the most common ones are
   defined as constants in this module. The when parameter is one of
   :data:`UCBTYPE_ENTRY`, :data:`UCBTYPE_EXIT` or :data:`UCBTYPE_REPLACE`. The
   function is a Python function which will accept the parameters that the OCI
   function accepts, modified as needed to return Python objects that are of
   some use. Note that this is a highly experimental method and can cause
   cx_Oracle to crash if not used properly. In particular, the OCI does not
   provide sizing information to the callback so attempts to access a variable
   beyond the allocated size will crash cx_Oracle.  Use with caution.

   .. note::

      This method is an extension to the DB API definition.


.. method:: Connection.rollback()

   Rollback any pending transactions.


.. method:: Connection.shutdown([mode])

   Shutdown the database. In order to do this the connection must connected as
   :data:`SYSDBA` or :data:`SYSOPER`. First shutdown using one of the
   DBSHUTDOWN constants defined in the constants (:ref:`constants`) section.
   Next issue the SQL statements required to close the database ("alter
   database close normal") and dismount the database ("alter database
   dismount") followed by a second call to this method with the
   :data:`DBSHUTDOWN_FINAL` mode.

   .. note::

      This method is an extension to the DB API definition and is only
      available in Oracle 10g R2 and higher.


.. method:: Connection.startup(force=False, restrict=False)

   Startup the database. This is equivalent to the SQL\*Plus command "startup
   nomount". The connection must be connected as :data:`SYSDBA` or
   :data:`SYSOPER` with the :data:`PRELIM_AUTH` option specified for this to
   work. Once this method has completed, connect again without the
   :data:`PRELIM_AUTH` option and issue the statements required to mount
   ("alter database mount") and open ("alter database open") the database.

   .. note::

      This method is an extension to the DB API definition and is only
      available in Oracle 10g R2 and higher.


.. attribute:: Connection.stmtcachesize

   This read-write attribute specifies the size of the statement cache. This
   value can make a significant difference in performance (up to 100x) if you
   have a small number of statements that you execute repeatedly.

   .. note::

      This attribute is an extension to the DB API definition.


.. method:: Connection.subscribe(namespace=cx_Oracle.SUBSCR_NAMESPACE_DBCHANGE, protocol=cx_Oracle.SUBSCR_PROTO_OCI, callback=None, timeout=0, operations=OPCODE_ALLOPS, rowids=False, port=0, qos=0, cqqos=0)

   Return a new Subscription object (:ref:`subscrobj`) using the connection.
   Currently the namespace and protocol arguments cannot have any other
   meaningful values. The callback is expected to be a callable that accepts
   a single argument which is a message object. The timeout value specifies
   that the subscription expires after the given time in seconds. The default
   value of 0 indicates that the subscription does not expire. The operations
   argument enables filtering of the messages that are sent (insert, update,
   delete). The rowids flag specifies whether the rowids of affected rows
   should be included in the messages that are sent. The port specifies the
   listening port for callback notifications from the database server. The qos
   argument specifies quality of service options common to all subscriptions.
   Currently the only meaningful option is cx_Oracle.SUBSCR_QOS_PURGE_ON_NTFN
   which indicates that the subscription should be automatically unregistered
   after the first notification. The default value of 0 indicates that the
   subscription should persist after notification. The cqqos argument specifies
   quality of service options specific to continuous query notification. The
   default value of 0 indicates that change notification is required at
   database object granularity. The flag cx_Oracle.SUBSCR_CQ_QOS_QUERY
   specifies that change notification is required at query result set
   granularity, and the flag SUBSCR_CQ_QOS_BEST_EFFORT specifies that best
   effort filtering is accpetable, and false positive notifications may be
   received.

   .. note::

      This method is an extension to the DB API definition and is only
      available in Oracle 10g R2 and higher.

   .. note::

      Query result set change notification is only available in Oracle 11g and
      higher.

   .. note::

      Do not close the connection before the subscription object is deleted or
      the subscription object will not be deregistered in the database. This is
      done automatically if connection.close() is never called.


.. attribute:: Connection.tnsentry

   This read-only attribute returns the TNS entry of the database to which a
   connection has been established.

   .. note::

      This attribute is an extension to the DB API definition.


.. method:: Connection.unregister(code, when)

   Unregister the function as an OCI callback. The code is one of the function
   codes defined in the Oracle documentation of which the most common ones are
   defined as constants in this module. The when parameter is one of
   :data:`UCBTYPE_ENTRY`, :data:`UCBTYPE_EXIT` or :data:`UCBTYPE_REPLACE`.

   .. note::

      This method is an extension to the DB API definition.


.. attribute:: Connection.username

   This read-only attribute returns the name of the user which established the
   connection to the database.

   .. note::

      This attribute is an extension to the DB API definition.


.. attribute:: Connection.version

   This read-only attribute returns the version of the database to which a
   connection has been established.

   .. note::

      This attribute is an extension to the DB API definition.

