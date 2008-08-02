%define name slsnif
%define version 0.4.4
%define release %mkrel 6

Summary: A serial sniffer 
Name: %{name}
Version: %{version}
Release: %{release}
Source0:  http://ovh.dl.sourceforge.net/sourceforge/slsnif/%{name}-%{version}.tar.gz
License: GPL 
Group: Monitoring
Url: http://sourceforge.net/projects/slsnif/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot


%description
A serial line sniffer

%prep
%setup -q

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING INSTALL NEWS README slsnifrc-example
%{_bindir}/slsnif
%{_mandir}/man1/slsnif.1*
