%define name slsnif
%define version 0.4.4
%define release 8

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


%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.4.4-7mdv2010.0
+ Revision: 433938
- rebuild

* Sat Aug 02 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.4.4-6mdv2009.0
+ Revision: 260820
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.4.4-5mdv2009.0
+ Revision: 252619
- rebuild

* Mon Mar 10 2008 Erwan Velu <erwan@mandriva.org> 0.4.4-3mdv2008.1
+ Revision: 183358
- Rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Sep 07 2007 Erwan Velu <erwan@mandriva.org> 0.4.4-2mdv2008.0
+ Revision: 81687
- Rebuild
- Import slsnif




* Tue Aug 29 2006 Erwan Velu <erwan@seanodes.com> 0.4.4-1mdv2007.0
- Initial release 
