%global debug_package %{nil}

Name: acestream-engine
Version: 3.1.49
Release: 2%{?dist}
Summary: Ace Stream Engine
License: LGPL-2.0
Group: Productivity/Multimedia/Other
URL: http://acestream.org/

ExclusiveArch: x86_64

Source0: http://acestream.org/downloads/linux/acestream_%{version}_debian_9.9_x86_64.tar.gz
Patch1:  start-engine.patch

Requires: python2-setuptools python2-apsw
Recommends: python2-appindicator
Requires: fdk-aac
# optional
%if 0%{?fedora} && 0%{?fedora} <= 31
Requires: python2-beautifulsoup4 python2-blist python2-GeoIP python2-iso8601
Requires: python2-dns
Requires: python2-futures python2-lxml m2crypto python2-miniupnpc
Requires: python2-protobuf python2-psutil
Requires: python2-webencodings
Requires: python2-typing
# python-bitarray-1.x is not compatible
#Requires: python-bitarray
Requires: python2-requests
Requires: python2-six
Requires: python2-enum34
%endif

%description
Ace Stream is an engine which allows users to watch live streams and video based on torrent protocol.

%prep
%setup -qc
%patch1 -p1
cd lib
%if 0%{?fedora} && 0%{?fedora} <= 31
rm beautifulsoup4-4.5.3-py2.7.egg
rm blist-1.3.4-py2.7-linux-x86_64.egg
rm dnspython-1.15.0-py2.7.egg
rm enum34-1.1.6-py2.7.egg
rm GeoIP-1.3.2-py2.7-linux-x86_64.egg
rm iso8601-0.1.10-py2.7.egg
rm futures-3.0.5-py2.7.egg
rm lxml-3.7.2-py2.7-linux-x86_64.egg
rm M2Crypto-0.35.2-py2.7-linux-x86_64.egg
rm miniupnpc-2.1-py2.7-linux-x86_64.egg
rm protobuf-3.0.0b2-py2.7.egg
rm psutil-1.2.1-py2.7-linux-x86_64.egg
rm requests-2.12.5-py2.7.egg
rm six-1.10.0-py2.7.egg
rm typing-3.7.4-py2.7.egg
rm webencodings-0.5-py2.7.egg
rm websocket_client-0.40.0-py2.7.egg
%endif
cd -

%build

%install
%__mkdir_p %{buildroot}/opt/%{name}
%__mkdir_p %{buildroot}%{_bindir}
%__install -m 755 acestreamengine %{buildroot}/opt/%{name}
%__install -m 755 start-engine %{buildroot}/opt/%{name}
%__cp -a acestream.conf %{buildroot}/opt/%{name}
%__cp -a data lib %{buildroot}/opt/%{name}
%__ln_s ../../opt/%{name}/start-engine %{buildroot}%{_bindir}/acestreamengine
touch %{buildroot}/opt/%{name}/acestream.log
%__chmod 777 %{buildroot}/opt/%{name}/acestream.log
 
%files
/opt/%{name}/
%{_bindir}/acestreamengine
 
%changelog
* Thu Dec 19 2019 Sérgio Basto <sergio@serjux.com> - 3.1.49-2
- Try to deal with python2 mass removal on F32

* Thu Dec 19 2019 Sérgio Basto <sergio@serjux.com> - 3.1.49-1
- Update to 3.1.49

